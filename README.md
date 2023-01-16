# private-container-image-repo

In the private_repo_deployment.yml here(https://github.com/devtoprod-jsm/private-container-image-repo/blob/41b9f737512e57613a15bd806bc08ebf660bf849/private_repo_deployment.yml#L20) make the changes according to where you have created the "registry" (need to create this directory) directory.

Follow the below command line instructions to deploy the private repo deployment and expose it as a nodeport service on your local environment.

$ kubectl apply -f private_repo_deployment.yml
$ kubectl apply -f private_repo_svc.yml

Example push scenario to your local private repository.

I am downloading nginx image from the dockerhub repository here, you can use the one you developed from your docker file.
$ docker pull nginx
Tag the image to the private repository
$ docker tag nginx:latest localhost:31320/nginx:1.17
Push the image to the private repository.
$ docker push localhost:31320/nginx:1.17
Test the pushed image by deploying it.
kubectl apply -f nginx-test-deploy.yml

##############
Build and push py app to private repo
$ docker build -t demo-py-app:1.0.0 .
$ docker tag demo-py-app:1.0.0 localhost:31320/demo-py-app:1.0.0
$ docker push localhost:31320/demo-py-app:1.0.0

Create helm chart, modify the defaults to matchyour requirements.
$ helm create interview-demo

Chart installation, create namespace if not present (--create-namespace). Good to do a dry run before installing(use --dry-run)
Use: helm upgrade --install --create-namespace -n <namespace> -f environments/<environment>-values.yaml <your_release_name> <your_chart_path>
$ helm upgrade --install test ./my-interview-demo (using default values file, use the values file based on environment)
