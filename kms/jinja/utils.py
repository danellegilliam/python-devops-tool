from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def create_kms_key(**kwargs):
    env.globals['bucket_name'] = kwargs['bucket_name']
    env.globals['key_policy'] = kwargs['key_policy']
    env.globals['user_name'] = kwargs['user_name']
    template = env.get_template('kms.yml.j2')
    output = template.render()
    print(output)


create_kms_key(bucket_name='aaa', key_policy='bbb', user_name='ccc')
