resource "google_container_cluster" "primary" {
  name = "quotes-api"
  network = "default"
  location = "southamerica-east1"
  initial_node_count = 1
}