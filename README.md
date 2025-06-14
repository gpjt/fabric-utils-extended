# Fabric Utils Extended

An extended Fabric Connection class with additional utilities for SSH operations and deployment automation.

## Features

- **Password and Key Authentication**: Supports both password and SSH key authentication
- **Sudo File Transfer**: Upload files with sudo privileges using `put_sudo()`
- **Template Interpolation**: Upload files with variable interpolation using `put_interpolated()`
- **Remote Reboots**: Convenient `reboot()` method with configurable timeout
- **Enhanced Put Method**: Unified `put()` method that can optionally use sudo

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/gpjt/fabric-utils-extended.git
```

Or add to your `requirements.txt`:

```
git+https://github.com/gpjt/fabric-utils-extended.git
```

## Usage

### Basic Usage

```python
from fabric_utils import ExtendedConnection

# Connect with password
conn = ExtendedConnection('hostname', 'username', password='your_password')

# Connect with SSH key
conn = ExtendedConnection('hostname', 'username', key=your_private_key)
```

### File Transfer with Sudo

```python
# Regular file transfer
conn.put('local_file.txt', '/remote/path/file.txt')

# File transfer with sudo privileges
conn.put('local_file.txt', '/etc/config.conf', use_sudo=True)

# Or use put_sudo directly
conn.put_sudo('local_file.txt', '/etc/config.conf')
```

### Template Interpolation

```python
# Upload a template file with variable substitution
interpolation_vars = {
    'database_host': 'db.example.com',
    'api_key': 'your_api_key_here'
}

conn.put_interpolated(
    'config.template',
    '/etc/app/config.py',
    interpolation_vars,
    use_sudo=True
)
```

### Remote Reboot

```python
# Reboot with default 10 second timeout
conn.reboot()

# Reboot with custom timeout
conn.reboot(timeout=30)
```

## API Reference

### ExtendedConnection

Extends `fabric.Connection` with additional methods and functionality.

#### Constructor

```python
ExtendedConnection(host, user, password=None, key=None, **kwargs)
```

- `host`: Remote hostname or IP address
- `user`: Username for authentication
- `password`: Password for authentication (optional)
- `key`: SSH private key for authentication (optional)
- `**kwargs`: Additional arguments passed to `fabric.Connection`

#### Methods

##### `put(local_path_or_content, remote_path, use_sudo=False, **kwargs)`

Upload a file or content to the remote system.

- `local_path_or_content`: Local file path or file-like object
- `remote_path`: Destination path on remote system
- `use_sudo`: Whether to use sudo for the transfer
- `**kwargs`: Additional arguments passed to `fabric.Connection.put`

##### `put_sudo(local_path_or_content, remote_path, **kwargs)`

Upload a file with sudo privileges by using a temporary file.

##### `put_interpolated(local_path, remote_path, interpolation, use_sudo=False, **kwargs)`

Upload a file with template variable substitution.

- `local_path`: Path to template file
- `remote_path`: Destination path on remote system
- `interpolation`: Dictionary of variables for template substitution
- `use_sudo`: Whether to use sudo for the transfer

##### `reboot(timeout=10)`

Reboot the remote system and wait for the specified timeout.

- `timeout`: Time to wait after issuing reboot command (seconds)

## Requirements

- Python 3.7+
- fabric >= 2.0.0

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
