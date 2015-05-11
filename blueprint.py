def build(infrastructure):
    instance = infrastructure.create_instance('web-server')

    instance.provision()
    instance.setup_generic_php()

    instance.clone_project('git@github.com:istvan-antal/constructor-example-nginx-php.git')

    instance.use_nginx_config('nginx.conf')

    instance.install_my_key()