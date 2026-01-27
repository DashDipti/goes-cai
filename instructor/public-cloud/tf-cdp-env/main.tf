terraform {
  required_version = ">= 1.5.7"
  required_providers {
    cdp = {
      source  = "cloudera/cdp"
      version = "0.9.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  # ignore tags created by data services
  ignore_tags {
    key_prefixes = ["kubernetes.io/cluster"]
  }
}

module "cdp_deploy" {
    source = "git::https://github.com/cloudera-labs/cdp-tf-quickstarts.git//aws"
    
    env_prefix = var.env_prefix
    aws_region = var.aws_region
    
    ingress_extra_cidrs_and_ports = var.ingress_extra_cidrs_and_ports

    deployment_template = var.deployment_template
    datalake_scale      = var.datalake_scale   
    cdp_groups          = var.cdp_groups
  
    env_tags = var.env_tags
}

##### Support 'attaching' an extra buckets to the environment #####
  # Use the CDP Terraform Provider to find the xaccount account, external ids and policy contents
  data "cdp_environments_aws_credential_prerequisites" "cdp_prereqs" {}

  # ...process placeholders in the policy doc
  locals {
    data_bucket_access_policy_doc   = base64decode(data.cdp_environments_aws_credential_prerequisites.cdp_prereqs.policies["Bucket_Access"])

    extra_bucket_access_policies = [
      for bucket in var.extra_s3_buckets :
        replace(
    replace(
    local.data_bucket_access_policy_doc, "$${ARN_PARTITION}", "aws"),
  "$${DATALAKE_BUCKET}", bucket)
    ]  
  }

  # ...create the extra policies
resource "aws_iam_policy" "cdp_extra_bucket_data_access_policy" {

  count = length(var.extra_s3_buckets)

  name        = "${var.env_prefix}-extra-data-policy-${var.extra_s3_buckets[count.index]}"
  description = "CDP Data Access for additional bucket ${var.extra_s3_buckets[count.index]}"

  tags = merge(var.env_tags, { Name = "${var.env_prefix}-extra-data-policy-${var.extra_s3_buckets[count.index]}" })

  policy = local.extra_bucket_access_policies[count.index]

}

# Attach policy to DL admin role
resource "aws_iam_role_policy_attachment" "cdp_datalake_admin_role_extra_bucket" {

  for_each = { for k , v in aws_iam_policy.cdp_extra_bucket_data_access_policy: k => v}

  # role       = module.cdp_deploy.aws_datalake_admin_role_name # TODO: Need to expose this as a variable
  role       = "${var.env_prefix}-dladmin-role"
  policy_arn = each.value.arn

  depends_on = [ module.cdp_deploy ]
}
