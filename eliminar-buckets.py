""" Elimina buckets versionados """
import sys

import boto3

BUCKETS = [
    "pfg-sia-afore-aims-entrada",
    "pfg-sia-afore-aims-salida",
    "pfg-sia-afore-flujo-caja-cloudtrail",
    "pfg-sia-afore-flujo-caja-entrada",
    "pfg-sia-afore-flujo-caja-proceso",
    "pfg-sia-afore-flujo-caja-salida",
    "pfg-sia-afore-intcash-entrada",
    "pfg-sia-afore-intcash-salida",
    "pfg-sia-afore-intcash-santander-entrada",
    "pfg-sia-afore-intcash-santander-salida",
    "pfg-sia-afore-md-entrada",
    "pfg-sia-afore-md-proceso",
    "pfg-sia-afore-md-salida",
    "pfg-sia-afore-mo-proceso",
    "pfg-sia-afore-mo-salida",
    "pfg-sia-comun-entrada-insumos",
    "pfg-sia-comun-salida-insumos",
    "pfg-sia-comun-sincronizacion-archivos-cloudtrail",
    "pfg-sia-fondos-crd-entrada",
    "pfg-sia-fondos-crd-salida",
    "pfg-sia-fondos-flujo-caja-cloudtrail",
    "pfg-sia-fondos-flujo-caja-entrada",
    "pfg-sia-fondos-flujo-caja-proceso",
    "pfg-sia-fondos-flujo-caja-salida",
    "pfg-sia-fondos-mandatos-entrada",
    "pfg-sia-fondos-mandatos-salida",
]

TEST = ["pfg-sia-test-delete-bucket"]

session = boto3.Session()
s3_client = session.client("s3")
s3_resource = session.resource("s3")

ambiente = sys.argv[1]
print(f"Ambiente: {ambiente}")

for bucket in TEST:
    bucket_name = bucket + "-" + ambiente
    try:
        print("===>" + bucket_name)
        response = s3_client.head_bucket(Bucket=bucket_name)
        print(response)
        print("Vaciando bucket")
        bucket = s3_resource.Bucket(bucket_name)
        response = bucket.object_versions.delete()
        print(response)
        print("Borrando bucket")
        response = s3_client.delete_bucket(Bucket=bucket_name)
        print(response)
    except Exception as e:
        print(f"**** Error al borrar el bucket {bucket_name}")
        print(e)
        continue
