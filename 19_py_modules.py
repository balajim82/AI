"""
In Python enterprise-level or large projects, the application is usually divided into multiple modules to keep the code organized and maintainable. Recently, I completed a project where I followed this approach.

GitHub Link: https://github.com/balajim82/AI/tree/genai-elite-projects/inventory-mgmt-cli-proj

In this project, the codebase is divided into different modules such as Controller, Service, Repository, Database, and Models.

Key practices followed in the project:

Every project should include a virtual environment (venv) setup.
Use a requirements.txt file to install all the required libraries.
Maintain a well-structured project layout with properly organized modules.
To communicate between modules or use third-party libraries, use the from and import keywords.

Example:

from src.repositories.inv_mgmt_opr_log_repository import InventoryMgmtOprLogRepository
src.repositories.inv_mgmt_opr_log_repository → Folder path and file name
InventoryMgmtOprLogRepository → Class or function that we want to access
Each module/file can include:
if __name__ == "__main__":

This allows the file to be executed independently, making it easier to test that specific module.
    
    
"""