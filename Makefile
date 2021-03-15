.PHONY: push, pull

pull:
	mkdir -p ../xyz-ekiim-api-storage
	gsutil rsync -R gs://xyz-ekiim-api-storage ../xyz-ekiim-api-storage
