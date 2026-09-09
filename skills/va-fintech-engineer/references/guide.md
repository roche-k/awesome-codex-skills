# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

Fintech engineering checklist:
- Transaction accuracy 100% verified
- System uptime > 99.99% achieved
- Latency < 100ms maintained
- PCI DSS compliance certified
- Audit trail comprehensive
- Security measures hardened
- Data encryption implemented
- Regulatory compliance validated

Banking system integration:
- Core banking APIs
- Account management
- Transaction processing
- Balance reconciliation
- Statement generation
- Interest calculation
- Fee processing
- Regulatory reporting

Payment processing systems:
- Gateway integration
- Transaction routing
- Authorization flows
- Settlement processing
- Clearing mechanisms
- Chargeback handling
- Refund processing
- Multi-currency support

Trading platform development:
- Order management systems
- Matching engines
- Market data feeds
- Risk management
- Position tracking
- P&L calculation
- Margin requirements
- Regulatory reporting

Regulatory compliance:
- KYC implementation
- AML procedures
- Transaction monitoring
- Suspicious activity reporting
- Data retention policies
- Privacy regulations
- Cross-border compliance
- Audit requirements

Financial data processing:
- Real-time processing
- Batch reconciliation
- Data normalization
- Transaction enrichment
- Historical analysis
- Reporting pipelines
- Data warehousing
- Analytics integration

Risk management systems:
- Credit risk assessment
- Fraud detection
- Transaction limits
- Velocity checks
- Pattern recognition
- ML-based scoring
- Alert generation
- Case management

Fraud detection:
- Real-time monitoring
- Behavioral analysis
- Device fingerprinting
- Geolocation checks
- Velocity rules
- Machine learning models
- Rule engines
- Investigation tools

KYC/AML implementation:
- Identity verification
- Document validation
- Watchlist screening
- PEP checks
- Beneficial ownership
- Risk scoring
- Ongoing monitoring
- Regulatory reporting

Blockchain integration:
- Cryptocurrency support
- Smart contracts
- Wallet integration
- Exchange connectivity
- Stablecoin implementation
- DeFi protocols
- Cross-chain bridges
- Compliance tools

Open banking APIs:
- Account aggregation
- Payment initiation
- Data sharing
- Consent management
- Security protocols
- API versioning
- Rate limiting
- Developer portals

## Development Workflow

Execute fintech development through systematic phases:

### 1. Compliance Analysis

Understand regulatory requirements and security needs.

Analysis priorities:
- Regulatory landscape
- Compliance requirements
- Security standards
- Data privacy laws
- Integration requirements
- Performance needs
- Scalability planning
- Risk assessment

Compliance evaluation:
- Jurisdiction requirements
- License obligations
- Reporting standards
- Data residency
- Privacy regulations
- Security certifications
- Audit requirements
- Documentation needs

### 2. Implementation Phase

Build financial systems with security and compliance.

Implementation approach:
- Design secure architecture
- Implement core services
- Add compliance layers
- Build audit systems
- Create monitoring
- Test thoroughly
- Document everything
- Prepare for audit

Fintech patterns:
- Security first design
- Immutable audit logs
- Idempotent operations
- Distributed transactions
- Event sourcing
- CQRS implementation
- Saga patterns
- Circuit breakers

### 3. Production Excellence

Ensure financial systems meet regulatory and operational standards.

Excellence checklist:
- Compliance verified
- Security audited
- Performance tested
- Disaster recovery ready
- Monitoring comprehensive
- Documentation complete
- Team trained
- Regulators satisfied

Transaction processing:
- ACID compliance
- Idempotency handling
- Distributed locks
- Transaction logs
- Reconciliation
- Settlement batches
- Error recovery
- Retry mechanisms

Security architecture:
- Zero trust model
- Encryption at rest
- TLS everywhere
- Key management
- Token security
- API authentication
- Rate limiting
- DDoS protection

Microservices patterns:
- Service mesh
- API gateway
- Event streaming
- Saga orchestration
- Circuit breakers
- Service discovery
- Load balancing
- Health checks

Data architecture:
- Event sourcing
- CQRS pattern
- Data partitioning
- Read replicas
- Cache strategies
- Archive policies
- Backup procedures
- Disaster recovery

Monitoring and alerting:
- Transaction monitoring
- Performance metrics
- Error tracking
- Compliance alerts
- Security events
- Business metrics
- SLA monitoring
- Incident response
