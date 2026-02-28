import io
import os
import time
from fabric import Connection


class ExtendedConnection(Connection):

    def __init__(self, host, user, password=None, key=None, **kwargs):
        connect_kwargs = kwargs.pop('connect_kwargs', {})
        if password:
            connect_kwargs['password'] = password
        if key:
            connect_kwargs['pkey'] = key

        super().__init__(host=host, user=user, connect_kwargs=connect_kwargs, **kwargs)

        if password:
            self.config.sudo.password = password


    def put(self, local_path_or_content, remote_path, use_sudo=False, **kwargs):
        if use_sudo:
            return self.put_sudo(local_path_or_content, remote_path, **kwargs)
        return super().put(local_path_or_content, remote_path, **kwargs)


    def put_sudo(self, local_path_or_content, remote_path, **kwargs):
        temp_name = f"/tmp/{os.path.basename(remote_path)}.{os.getpid()}"
        result = super().put(local_path_or_content, temp_name, **kwargs)
        self.sudo(f"mv {temp_name} {remote_path}")
        return result


    def put_interpolated(self, local_path, remote_path, interpolation, use_sudo=False, **kwargs):
        with open(local_path, "r", encoding="utf-8", newline="") as f:
            content = f.read()
        rendered = content.format(**interpolation)

        # Optional but nice: normalize line endings so size is deterministic
        rendered = rendered.replace("\r\n", "\n")

        interpolated_bytes = io.BytesIO(rendered.encode("utf-8"))
        return self.put(interpolated_bytes, remote_path, use_sudo=use_sudo, **kwargs)

    def reboot(self, timeout=10):
        self.sudo("reboot", warn=True)
        time.sleep(timeout)
