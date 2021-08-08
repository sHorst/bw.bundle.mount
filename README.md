# bw.bundle.mount

## defaults
```python
metadata = {
    'mount': {
        'discs': [
            # /dev/mapper/fry-root                            /                                               ext4    discard,noatime,errors=remount-ro       0       1
            {
                'file_system': '/dev/mapper/fry-root',
                'mount_point': '/',
                'type': 'ext4',
                'options': ['discard', 'noatime', 'errors=remount-ro'],
                'pass': 1,
            },
            # UUID=c4c7e595-4c96-4a43-9629-e4316a9da0fc       /boot                                           ext2    defaults                                0       2
            {
                'file_system': 'UUID=c4c7e595-4c96-4a43-9629-e4316a9da0fc',
                'mount_point': '/boot',
                'type': 'ext2',
                'options': ['defaults'],
                'pass': 2,
            },
        ],

        'binds': [
            {'from': '/mnt/test123', 'to': '/home/test123', },
        ],

        'swap': [
            # /mnt/raid/swapfile1                             none                                            swap    sw                                      0       0
            {'file_system': '/mnt/raid/swapfile1', 'options': ['sw']},
        ],

        'tmp': [
            # tmpfs                                           /tmp                                            tmpfs   defaults,size=64g                       0       0
            {'mount_point': '/tmp', 'size': '64g', },
        ],

        'network': [
            # 192.168.2.123:/                                /mnt/raid                                        nfs     defaults                                0       0
            {
                'server': '192.168.2.123:/',
                'mount_point': '/mnt/raid',
                'type': 'nfs',
                'options': ['defaults'],
            },
        ],
    },
}

```