FROM ros:humble-ros-base

# Çalışma dizini
WORKDIR /ws

# Gereken paketler
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Proje dosyalarını çalışma alanına kopyala
COPY src /ws/src

# ROS2 ortamını yükle & build et
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

# entrypoint.sh dosyasını ekle
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
