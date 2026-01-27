# ------- Global settings -------
variable "aws_region" {
  type        = string
  description = "Region which Cloud resources will be created"
}

variable "env_prefix" {
  type        = string
  description = "Shorthand name for the environment. Used in resource descriptions"
}

variable "env_tags" {
  type        = map(any)
  description = "Tags applied to pvovisioned resources"

  default = null
}

# ------- CDP Environment Deployment -------
variable "deployment_template" {
  type = string

  description = "Deployment Pattern to use for Cloud resources and CDP"
}

variable "datalake_scale" {
  type = string

  description = "The scale of the datalake. Valid values are LIGHT_DUTY, ENTERPRISE."

  validation {
    condition     = (var.datalake_scale == null ? true : contains(["LIGHT_DUTY", "ENTERPRISE", "MEDIUM_DUTY_HA"], var.datalake_scale))
    error_message = "Valid values for var: datalake_scale are (LIGHT_DUTY, ENTERPRISE, MEDIUM_DUTY_HA)."
  }

  default = null

}

variable "ingress_extra_cidrs_and_ports" {
  type = object({
    cidrs = list(string)
    ports = list(number)
  })
  description = "List of extra CIDR blocks and ports to include in Security Group Ingress rules"

  default = null
}

variable "cdp_groups" {
  type = set(object({
    name                          = string
    create_group                  = bool
    sync_membership_on_user_login = optional(bool)
    add_id_broker_mappings        = bool
    })
  )

  description = "List of CDP Groups to be added to the IDBroker mappings of the environment. If create_group is set to true then the group will be created."

  validation {
    condition = (var.cdp_groups == null ? true : alltrue([
      for grp in var.cdp_groups :
      length(grp.name) >= 1 && length(grp.name) <= 64
    ]))
    error_message = "The length of all CDP group names must be 64 characters or less."
  }
  validation {
    condition = (var.cdp_groups == null ? true : alltrue([
      for grp in var.cdp_groups :
      can(regex("^[a-zA-Z0-9\\-\\_\\.]{1,90}$", grp.name))
    ]))
    error_message = "CDP group names can consist only of letters, numbers, dots (.), hyphens (-) and underscores (_)."
  }

  default = null
}

# ------- Extra S3 buckets to attach to the CDP Environment -------
variable "extra_s3_buckets" {
  type = list(string)
  description = "List of additional S3 buckets to make available for access from the CDP datalake"
  
  default = []
}