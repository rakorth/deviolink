class SystemInfoView:
    def __init__(self, software_type: str, software_version: str, hardware_device_id: str, device_config_name: str,
                 in_safe_mode: bool, safe_mode_err_msg: str):
        self.software_type = software_type
        self.software_version = software_version
        self.hardware_device_id = hardware_device_id
        self.device_config_name = device_config_name
        self.in_safe_mode = in_safe_mode
        self.safe_mode_err_msg = safe_mode_err_msg

    def to_dict(self):
        return {
            '__type': 'system_info',
            'software_type': self.software_type,
            'software_version': self.software_version,
            'hardware_device_id': self.hardware_device_id,
            'device_config_name': self.device_config_name,
            'in_safe_mode': self.in_safe_mode,
            'safe_mode_err_msg': self.safe_mode_err_msg
        }
