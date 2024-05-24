terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.30.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "goodreads_datalake" {
  name          = "goodreads-book-reviews"
  location      = var.region
  storage_class = var.storage_class

  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_bigquery_dataset" "goodreads_external_dataset" {
  project                    = var.project
  location                   = var.region
  dataset_id                 = var.goodreads_external_datasets
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "goodreads_analytics_dataset" {
  project                    = var.project
  location                   = var.region
  dataset_id                 = var.goodreads_analytics_datasets
  delete_contents_on_destroy = true
}
