terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.30.0"
    }
  }
}

provider "google" {
  project = local.envs["PROJECT_ID"]
  region  = var.region
}

resource "google_storage_bucket" "goodreads_datalake" {
  name          = "goodreads-book-reviews"
  location      = var.region
  storage_class = var.storage_class

  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "goodreads_external_dataset" {
  project                    = local.envs["PROJECT_ID"]
  location                   = var.region
  dataset_id                 = var.goodreads_external_datasets
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "goodreads_analytics_dataset" {
  project                    = local.envs["PROJECT_ID"]
  location                   = var.region
  dataset_id                 = var.goodreads_analytics_datasets
  delete_contents_on_destroy = true
}
