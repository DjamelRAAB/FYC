output "azurerm_container_registry_id" {
    value = azurerm_container_registry.acr.id
}
output "azurerm_container_registry_name" {
    value = azurerm_container_registry.acr.name
}
output "azurerm_container_registry_admin_username" {
    value = azurerm_container_registry.acr.admin_username
}

output "azurerm_container_registry_admin_password" {
    value = azurerm_container_registry.acr.admin_password
}