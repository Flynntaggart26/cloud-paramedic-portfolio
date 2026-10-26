# Risks for Paramedics and Field Health Teams

## Result
Cloud technology can improve speed, sharing, and continuity. However, misapplied cloud design can expose patient data, break continuity during outages, or create compliance issues.

## Main risk areas
- **Data exposure**: patient data can be leaked via misconfigured storage, logs, or shared links.
- **Compliance**: HIPAA, GDPR, KVKK, and local health regulations may apply.
- **Downtime**: cloud provider outage can affect records, e-mail, and monitoring.
- **Backups**: loss or encryption of backups can interrupt continuity.
- **Identity and credentials**: weak passwords or leaked keys can cause unauthorized access.
- **Vendor lock-in**: high switching costs make it hard to move providers.
- **Data residency**: local data may need to remain in a specific country or region.
- **Environmental factors**: power, cooling, and physical security still matter.
- **Human factor**: phishing, mistakes, and local sharing of patient images.

## Preferred controls
- Encrypt data **in transit** and **at rest**.
- Use least privilege and multi-factor authentication.
- Maintain a 3-2-1 backup strategy: 3 copies, 2 media types, 1 offline/immutable copy.
- Test restore and downtime procedures.
- Keep offline/manual documentation mode for vehicle and incident use.
- Sign and review vendor agreements (BAA/AIAs) and data residency clauses.
- Train field staff and run incident simulations.

For an in-depth risk list, see `cloud-risks-paramedic.md`.
