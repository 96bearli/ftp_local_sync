# ftp_local_sync
A little ftp tool with python

## usage

```python
if __name__ == '__main__':
	# ftp ip...config
    host = "192.168.1.201"
    username = ""
    password = ""
    port = 21
    # target path
    ftp_file_path = "UserUpload"  # FTP dir
    dst_file_path = r"./"  # 本地目录 local
    this = FTP_OP(host=host, username=username, password=password, port=port)
    # sync
    this.whileTrue(sepTime=5)
    # once
    # ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)
```
