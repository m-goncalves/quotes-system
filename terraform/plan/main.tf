provider "google" {
    credentials       = file(var.credentials)
    project           = var.project
    region            = var.region
}

resource "google_container_cluster" "primary" {
  name                = var.cluster_name
  network             = var.network
  location            = var.region
  initial_node_count  = var.initial_node_count
}

resource "google_container_node_pool" "primary_preemtible_nodes" {
  name                = var.node_name
  location            = var.region
  cluster             = google_container_cluster.primary.name
  node_count          = var.node_count

  node_config {
    preemptible       = var.preemptible
    machine_type      = var.machine_type
  }
}

resource "google_storage_bucket" "state_bucket"{
  name                = var.bucket_name 
  location            = var.region
  force_destroy       = true 
}

# data "terraform_remote_state" "quotes-state" {
#   backend             = "gcs"
#   config              = {
#     bucket            = var.bucket_name
#     prefix            = var.prefix
#   }
# }