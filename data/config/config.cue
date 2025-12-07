package config

app: {
	name:    string | *"App"
	version: string | *"0.1.0"
}

logging: {
	level:  "DEBUG" | "INFO" | "WARNING" | "ERROR" | *"INFO"
	format: string | *"%(levelname)s: %(message)s"
}
