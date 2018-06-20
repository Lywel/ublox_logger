# ublox_logger

  1) Launch the ublox ros node
  ```bash
  roslaunch ublox_gps ublox_device.launch param_file_name:=c94_m8p_rover node_name:=ublox_gps_rover
  ```
  
  2) Lauch the logger ros node
  
  ```bash
  roslaunch ublox_logger start.launch
  ```
