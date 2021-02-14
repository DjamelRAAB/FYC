output "azurerm_resource_group_name" {
    value = azurerm_resource_group.fyc.name
}

output "azurerm_container_registry_name" {
    value = module.registry.azurerm_container_registry_name
}
output "azurerm_container_registry_admin_username" {
    value = module.registry.azurerm_container_registry_admin_username
}

output "azurerm_container_registry_admin_password" {
    value = module.registry.azurerm_container_registry_admin_password
}