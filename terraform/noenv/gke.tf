resource "google_container_cluster" "primary" {
  name = "quotes-api"
  network = "default"
  location = "southamerica-east1"
  initial_node_count = 1
}

resource "google_container_node_pool" "primary_preemtible_nodes" {
  name = "node-pool"
  location = var.location
  cluster = "google_container_cluster.primary.name"
  node_count = 2

  node_config {
    preemptible = false
    machine_type = "n1-standard-1"
  }
}