variable "project" {
  type        = string
  description = "ID do Projeto"
  default     = "book-recommendation-424220"
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
  default     = "goodreads_wh"
}

variable "goodreads_analytics_datasets" {
  type        = string
  description = "Dataset no BigQuery para os dados do GCS e DBT."
  default     = "goodreads_analytics"
}
