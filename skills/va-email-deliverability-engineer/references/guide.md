# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

Email deliverability checklist:
- SPF, DKIM, and DMARC aligned and passing verified
- Bounce rate maintained below 2% consistently
- Spam complaint rate kept below 0.1% strictly
- Inbox placement rate tracked across major mailbox providers
- List hygiene and suppression automated reliably
- Sending domains warmed up gradually before full volume
- Unsubscribe and suppression requests honored within 24 hours
- Sender reputation monitored continuously across blocklists

Authentication and identity:
- SPF record scope and lookup limits
- DKIM key rotation and selector management
- DMARC policy staging (none to quarantine to reject)
- DMARC aggregate and forensic report parsing
- BIMI eligibility and VMC requirements
- Custom tracking domain alignment
- Subdomain strategy for transactional vs marketing
- Multi-provider SPF flattening

Sending infrastructure:
- Dedicated vs shared IP tradeoffs
- IP and domain warm-up schedules
- Volume ramping by ISP
- Feedback loop registration
- TLS and MTA-STS enforcement
- Return-path and bounce domain setup
- Sending time and cadence throttling
- Multi-region sending failover

Provider integration:
- Transactional send via nodemailer/SMTP
- Provider-agnostic evaluation (SES, SendGrid, Postmark, Mailgun)
- API vs SMTP relay tradeoffs
- Webhook handling for events
- Template rendering across clients
- Failover between providers
- Rate limit and retry handling
- Sandbox vs production credential separation

Bounce and complaint handling:
- Hard vs soft bounce classification
- Automatic suppression on hard bounce
- Complaint feedback loop processing
- Retry backoff for transient failures
- Bounce reason categorization
- Suppression list synchronization
- Re-engagement before removal
- Bounce rate alerting thresholds

List hygiene and suppression:
- Double opt-in verification
- Role-account and disposable-domain filtering
- Sunset policy for inactive addresses
- Suppression list deduplication
- Global vs per-campaign suppression
- Import-time validation
- Spam-trap avoidance
- List segmentation by engagement

Deliverability monitoring:
- Seed list inbox placement testing
- Blocklist monitoring and delisting
- ISP-specific postmaster tools
- Sender score tracking
- Engagement metrics (opens, clicks, complaints)
- Domain and IP reputation dashboards
- Anomaly detection on send patterns
- Competitive benchmark tracking

Compliance and rendering:
- CAN-SPAM header and footer requirements
- GDPR consent and data retention
- One-click unsubscribe (RFC 8058)
- Physical address disclosure
- Spam-trigger word avoidance
- Image-to-text ratio balance
- Dark mode and client rendering checks
- Accessibility of email markup

## Development Workflow

Execute email deliverability work through systematic phases:

### 1. Infrastructure Analysis

Understand current sending setup and reputation baseline.

Analysis priorities:
- Authentication record status
- Provider and IP configuration
- Historical bounce/complaint rates
- List quality and source
- Compliance obligations
- Existing monitoring gaps
- Volume and cadence patterns
- Risk assessment

Deliverability evaluation:
- Review DNS records
- Assess sender reputation
- Plan authentication rollout
- Define suppression rules
- Estimate warm-up timeline
- Plan monitoring coverage
- Document compliance gaps
- Prototype test sends

### 2. Implementation Phase

Build authenticated, monitored sending infrastructure.

Implementation approach:
- Authentication records
- Provider integration
- Bounce/complaint handlers
- List hygiene automation
- Warm-up scheduling
- Monitoring dashboards
- Compliance headers
- Template testing

Development patterns:
- Stage DMARC gradually
- Warm up before scaling
- Automate suppression
- Monitor continuously
- Document sending domains
- Isolate transactional from bulk
- Test across mailbox providers
- Compliance by default

### 3. Deliverability Excellence

Deliver reliable, compliant inbox placement.

Excellence checklist:
- Authentication fully aligned
- Bounce rate minimal
- Complaints negligible
- Inbox placement high
- Suppression automated
- Compliance verified
- Monitoring in place
- Reputation stable

Warm-up strategy:
- Gradual volume ramping
- Engaged-segment-first sending
- IP and domain pairing
- Daily volume caps
- ISP-specific pacing
- Reputation checkpoint gates
- Rollback triggers
- Warm-up completion criteria

Monitoring and alerting:
- Bounce rate thresholds
- Complaint rate thresholds
- Blocklist detection alerts
- Authentication failure alerts
- Volume anomaly detection
- Engagement drop alerts
- Provider outage detection
- Weekly reputation reports
