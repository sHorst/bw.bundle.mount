defaults = {}


@metadata_reactor
def add_nfs_apt(metadata):
    if not node.has_bundle("apt"):
        raise DoNotRunAgain

    types = [x.get('type', None) for x in metadata.get('mount/network', [])]
    packages = {}
    if 'nfs' in types:
        packages['nfs-common'] = {'installed': True, }

    return {
        'apt': {
            'packages': packages,
        }
    }


@metadata_reactor
def convert_typed_mounts_to_mount_points(metadata):
    # only manipulate metadata, if mount is set
    if metadata.get('mount', None) is None:
        return {}

    mounts = []

    mounts += [{'comment': 'discs'}]
    mounts += metadata.get('mount/discs', [])

    # add binds
    if 'binds' in metadata.get('mount', {}):
        mounts += [{'comment': ''}, {'comment': 'binds'}]
        for bind in metadata.get('mount/binds', []):
            options = bind.get('options', [])
            if 'bind' not in options:
                options += ['bind', ]

            mounts += [
                {
                    'file_system': bind['from'],
                    'mount_point': bind['to'],
                    'type': 'none',
                    'options': options,
                    'dump': 0,
                    'pass': 0,
                },
            ]

    # add swap
    if 'swap' in metadata.get('mount', {}):
        mounts += [{'comment': ''}, {'comment': 'swap'}]
        for swap in metadata.get('mount/swap', []):
            mounts += [
                {
                    'file_system': swap['file_system'],
                    'mount_point': 'none',
                    'type': 'swap',
                    'options': swap.get('options', ['sw']),
                    'dump': 0,
                    'pass': 0,
                },
            ]

    # add tmp
    if 'tmp' in metadata.get('mount', {}):
        mounts += [{'comment': ''}, {'comment': 'tmp'}]
        for tmp in metadata.get('mount/tmp', []):
            mounts += [
                {
                    'file_system': 'tmpfs',
                    'mount_point': tmp['mount_point'],
                    'type': 'tmpfs',
                    'options': ['defaults', 'size=' + tmp.get('size', '1g'), ],
                    'dump': 0,
                    'pass': 0,
                },
            ]

    # add network
    if 'network' in metadata.get('mount', {}):
        mounts += [{'comment': ''}, {'comment': 'network'}]
        for network in metadata.get('mount/network', []):
            mounts += [
                {
                    'file_system': network['server'],
                    'mount_point': network['mount_point'],
                    'type': network.get('type', 'nfs'),
                    'options': network.get('options', ['defaults']),
                    'dump': 0,
                    'pass': 0,
                },
            ]

    return {
        'mount': {
            'mounts': mounts,
        },
    }
