.PHONY: push, pull

# This value is the URI for the bucket or
# bucket with path corresponding to the storage you
# want to sync.
BUCKET_URI=gs://xyz-ekiim-api-storage

# This value is the local path for the directory
# where you are storing the copy of the bucket
# you are using for this proyect.
LOCAL_API_STORAGE=../xyz-ekiim-api-storage

pull:
	mkdir -p $(LOCAL_API_STORAGE)
	gsutil rsync -R $(BUCKET_URI) $(LOCAL_API_STORAGE)
