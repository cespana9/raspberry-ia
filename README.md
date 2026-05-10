# Proyecto raspberry-ia

![Logo Raspberry IA](images/rasperryIA.png)

Guía paso a paso para montar un entorno optimizado de inteligencia artificial en Raspberry Pi 5 usando Ubuntu 25, SSD NVMe, Docker y Ollama.

---

#  Paso 1: Preparar el sistema

## 1.1 Instalar Ubuntu 25 (64-bit)

Instala Ubuntu 25 en tu Raspberry Pi usando Raspberry Pi Imager.

Después del primer arranque:

```bash
sudo apt update && sudo apt upgrade -y

# Instalar dependencias básicas
sudo apt install -y curl wget git jq python3-pip

# Verificar arquitectura (debe ser aarch64)
uname -m
```

---

## 1.2 Configurar SSD NVMe (recomendado)

Si usas un SSD NVMe con adaptador PCIe:

```bash
# Ver discos
lsblk

# Esto borra el disco
sudo mkfs.ext4 /dev/nvme0n1

# Montaje
sudo mkdir /mnt/ssd
sudo mount /dev/nvme0n1 /mnt/ssd
```

Montaje automático:

```bash
echo '/dev/nvme0n1 /mnt/ssd ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

---

## 1.3 Migrar sistema de SD a NVMe (opcional)

Para clonar la SD al NVMe:

```bash
sudo dd if=/dev/mmcblk0 of=/dev/nvme0n1 bs=4M status=progress
```

---

## 1.4 Configuración avanzada NVMe

Verificar rendimiento

```bash
sudo apt install -y hdparm

sudo hdparm -t --direct /dev/mmcblk0
sudo hdparm -t --direct /dev/nvme0n1
```

Habilitar arranque desde NVMe

```bash
sudo rpi-eeprom-config --edit
```

Configurar:

```bash
[all]
BOOT_UART=1
POWER_OFF_ON_HALT=0
BOOT_ORDER=0xf416
PCIE_PROBE=1
```

Reiniciar:

```bash
sudo shutdown -r now
```

Ajustes de firmware

```bash
sudo vi /boot/firmware/config.txt
```

```bash
[all]

dtparam=nvme
dtparam=pciex1_gen=3
```



Expandir el sistema de archivos

```bash
sudo apt install -y cloud-guest-utils
sudo growpart /dev/nvme0n1 2
sudo resize2fs /dev/nvme0n1p2

df -hT
```
---

## 1.5 Optimizar el sistema para IA

Aumentamos la memoria swap para poder ejecutar modelos más grandes:

```
# Aumentar swap a 16GB

# Crear archivo de swap
sudo fallocate -l 16G /swapfile || \
sudo dd if=/dev/zero of=/swapfile bs=1M count=16384
sudo chmod 600 /swapfile
sudo mkswap /swapfile

grep -qF "/swapfile" /etc/fstab || echo "/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab

# Ajustar swappiness
sudo sysctl vm.swappiness=20
grep -qF "vm.swappiness" /etc/sysctl.conf || echo "vm.swappiness=20" | sudo tee -a /etc/sysctl.conf


# Verificar
free -h
```

  

---

#  Paso 2: Instalar Docker

Instalar dependencias:

```bash
sudo apt install -y ca-certificates curl gnupg

```

Añadir repositorio oficial:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Instalar Docker:

```bash
sudo apt update
sudo apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

Permisos:

```bash
sudo usermod -aG docker $USER
logout
```

---

# Paso 3: Instalar Ollama

## 3.1 Instalación automática

```bash
curl -fsSL https://ollama.com/install.sh | sh

# Verificar
ollama --version

# Estado del servicio
systemctl status ollama
```

---

## 3.2 Configurar acceso en red

Por defecto solo escucha en localhost. Lo abrimos:

```bash
sudo mkdir -p /etc/systemd/system/ollama.service.d
```

```bash
sudo tee /etc/systemd/system/ollama.service.d/override.conf << 'EOF'
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_ORIGINS=*"
EOF
```

Aplicar cambios:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Verificar:

```bash
curl http://localhost:11434/api/tags
```

---

## 3.3 Descargar modelos

Recomendados para Raspberry Pi 5 (8GB):

```bash
# LLM
ollama pull gemma4:e2b

ollama pull llama3.2:3b

# VLM
ollama pull moondream:latest 

ollama pull SmolVLM2-500M-Video-Instruct

```
Ver modelos:

```bash
ollama list
```
```bash
NAME                ID              SIZE      MODIFIED
moondream:latest    55fc3abd3867    1.7 GB    2 days ago
gemma4:e2b          7fbdbf8f5e45    7.2 GB    2 days ago
```
---

## 3.4 Configura el entorno:
```bash
chmod +x setup.sh && ./setup.sh
```


## 3.5 Uso
Activa el entorno: `source venv/bin/activate`
- Correr Visión: `python vlm/vision_app.py`
- Correr Chat: `python llm/chat_app.py`


# Resultado final

Tendrás:

* Sistema optimizado para IA
* SSD NVMe funcionando
* Docker instalado
* Ollama corriendo en red
* Modelos LLM locales funcionando

---