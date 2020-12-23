resource "google_container_cluster" "primary" {
  name = var.cluster_name
  network = var.network
  location = var.region
  initial_node_count = var.initial_node_count
}

resource "google_container_node_pool" "primary_preemtible_nodes" {
  name = var.node_name
  location = var.location
  cluster = "google_container_cluster.primary.name"
  node_count = 2

  node_config {
    preemptible = var.preemptible
    machine_type = var.machine_type
  }
}