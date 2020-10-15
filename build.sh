docker build --tag simon1000/carbontracker:latest ./trackerproject
docker push simon1000/carbontracker:latest
gcloud config set project impact-284220
gcloud compute instances reset carbontracker --zone=us-central1-a