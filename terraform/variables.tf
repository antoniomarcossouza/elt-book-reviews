locals {
  envs = { for tuple in regexall("(.*)=(.*)", file("../.env")) : tuple[0] => sensitive(tuple[1]) }
}

variable "region" {
  type        = string
  description = "Região dos recursos. https://googlecloudplatform.github.io/region-picker/"
  default     = "us-east1"
}

variable "storage_class" {
  type        = string
  description = "Storage Class do bucket. https://cloud.google.com/storage/docs/storage-classes"
  default     = "STANDARD"
}

variable "goodreads_external_datasets" {
  type        = string
  description = "Dataset no BigQuery para as external tables."
  default     = "goodreads_staging"
}

variable "goodreads_analytics_datasets" {
  type        = string
  description = "Dataset no BigQuery para os dados do GCS e DBT."
  default     = "goodreads_analytics"
}
