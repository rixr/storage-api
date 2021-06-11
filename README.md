# Bottle Storage Server

This is a minimal _HTTP API_ (_work in progress_) that allows you
to make use of _Google Cloud Storage_.

So far it only stores `json` and `files`.

To make use of this in your local environment you should have a
`gcloud_key.json` which you can generate from the Cloud Console.

Also you need to set the appreciate environment variables specified at
`example.env`.

_Suggestion:_ Copy `example.env` to `.env`, and then overwrite the values
in that file.

This project can be deployed as a _Google Cloud Run_ service.
