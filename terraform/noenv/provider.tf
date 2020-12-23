provider "google" {
    credentials     = file("auth/quotes-299423-3a622a0a01f1.json")
    project         = var.project
    region          = var.region
}