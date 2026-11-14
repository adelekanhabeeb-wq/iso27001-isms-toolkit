"""
ISO/IEC 27001:2022 Compliance-as-Code Evidence Collector
Control Mapping:
  - Annex A.8.24: Use of cryptography (Data at rest encryption)
  - Annex A.5.23: Information security for use of cloud services

Description:
  Audits all AWS S3 buckets in the account to verify default server-side
  encryption (SSE-S3 or SSE-KMS) is enabled and exports a timestamped JSON
  audit log for ISO 27001 surveillance audits.
"""

import json
from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError


def audit_s3_encryption() -> dict:
    """Checks default encryption status across all S3 buckets."""
    s3_client = boto3.client("s3")
    audit_timestamp = datetime.now(timezone.utc).isoformat()

    report = {
        "standard": "ISO/IEC 27001:2022",
        "controls": ["A.8.24", "A.5.23"],
        "audit_timestamp_utc": audit_timestamp,
        "summary": {"total_buckets": 0, "compliant": 0, "non_compliant": 0},
        "results": [],
    }

    buckets = s3_client.list_buckets().get("Buckets", [])
    report["summary"]["total_buckets"] = len(buckets)

    for bucket in buckets:
        bucket_name = bucket["Name"]
        try:
            enc = s3_client.get_bucket_encryption(Bucket=bucket_name)
            rules = enc["ServerSideEncryptionConfiguration"]["Rules"]
            algorithm = rules[0]["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]

            report["summary"]["compliant"] += 1
            report["results"].append(
                {
                    "bucket": bucket_name,
                    "status": "COMPLIANT",
                    "encryption_algorithm": algorithm,
                }
            )
        except ClientError as error:
            error_code = error.response["Error"]["Code"]
            if error_code == "ServerSideEncryptionConfigurationNotFoundError":
                report["summary"]["non_compliant"] += 1
                report["results"].append(
                    {
                        "bucket": bucket_name,
                        "status": "NON_COMPLIANT",
                        "reason": "Default server-side encryption not configured",
                    }
                )
            else:
                report["results"].append(
                    {
                        "bucket": bucket_name,
                        "status": "ERROR",
                        "reason": str(error),
                    }
                )

    return report


if __name__ == "__main__":
    audit_output = audit_s3_encryption()
    output_filename = f"s3_encryption_evidence_{datetime.now(timezone.utc).strftime('%Y%m%d')}.json"

    with open(output_filename, "w", encoding="utf-8") as file:
        json.dump(audit_output, file, indent=2)

    print(f"Audit complete. Summary: {audit_output['summary']}")
    print(f"Evidence saved to {output_filename}")
