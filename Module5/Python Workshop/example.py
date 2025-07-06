from fastavro.schema import load_schema

try:
    avro_schema = load_schema("avro_schema_json.avsc")
    print("Avro schema loaded successfully:", avro_schema)
except Exception as e:
    print(f"Failed to load Avro schema: {e}")