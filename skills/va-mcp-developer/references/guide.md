# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

MCP development checklist:
- Protocol compliance verified (JSON-RPC 2.0)
- Schema validation implemented
- Transport mechanism optimized
- Security controls enabled
- Error handling comprehensive
- Documentation complete
- Testing coverage > 90%
- Performance benchmarked

Server development:
- Resource implementation
- Tool function creation
- Prompt template design
- Transport configuration
- Authentication handling
- Rate limiting setup
- Logging integration
- Health check endpoints

Client development:
- Server discovery
- Connection management
- Tool invocation handling
- Resource retrieval
- Prompt processing
- Session state management
- Error recovery
- Performance monitoring

Protocol implementation:
- JSON-RPC 2.0 compliance
- Message format validation
- Request/response handling
- Notification processing
- Batch request support
- Error code standards
- Transport abstraction
- Protocol versioning

SDK mastery:
- TypeScript SDK usage
- Python SDK implementation
- Schema definition (Zod/Pydantic)
- Type safety enforcement
- Async pattern handling
- Event system integration
- Middleware development
- Plugin architecture

Integration patterns:
- Database connections
- API service wrappers
- File system access
- Authentication providers
- Message queue integration
- Webhook processors
- Data transformation
- Legacy system adapters

Security implementation:
- Input validation
- Output sanitization
- Authentication mechanisms
- Authorization controls
- Rate limiting
- Request filtering
- Audit logging
- Secure configuration

Performance optimization:
- Connection pooling
- Caching strategies
- Batch processing
- Lazy loading
- Resource cleanup
- Memory management
- Profiling integration
- Scalability planning

Testing strategies:
- Unit test coverage
- Integration testing
- Protocol compliance tests
- Security testing
- Performance benchmarks
- Load testing
- Regression testing
- End-to-end validation

Deployment practices:
- Container configuration
- Environment management
- Service discovery
- Health monitoring
- Log aggregation
- Metrics collection
- Alerting setup
- Rollback procedures

## Development Workflow

Execute MCP development through systematic phases:

### 1. Protocol Analysis

Understand MCP requirements and architecture needs.

Analysis priorities:
- Data source mapping
- Tool function requirements
- Client integration points
- Transport mechanism selection
- Security requirements
- Performance targets
- Scalability needs
- Compliance requirements

Protocol design:
- Resource schemas
- Tool definitions
- Prompt templates
- Error handling
- Authentication flows
- Rate limiting
- Monitoring hooks
- Documentation structure

### 2. Implementation Phase

Build MCP servers and clients with production quality.

Implementation approach:
- Setup development environment
- Implement core protocol handlers
- Create resource endpoints
- Build tool functions
- Add security controls
- Implement error handling
- Add logging and monitoring
- Write comprehensive tests

MCP patterns:
- Start with simple resources
- Add tools incrementally
- Implement security early
- Test protocol compliance
- Optimize performance
- Document thoroughly
- Plan for scale
- Monitor in production

### 3. Production Excellence

Ensure MCP implementations are production-ready.

Excellence checklist:
- Protocol compliance verified
- Security controls tested
- Performance optimized
- Documentation complete
- Monitoring enabled
- Error handling robust
- Scaling strategy ready
- Community feedback integrated

Server architecture:
- Modular design
- Plugin system
- Configuration management
- Service discovery
- Health checks
- Metrics collection
- Log aggregation
- Error tracking

Client integration:
- SDK usage patterns
- Connection management
- Error handling
- Retry logic
- Caching strategies
- Performance monitoring
- Security controls
- User experience

Protocol compliance:
- JSON-RPC 2.0 adherence
- Message validation
- Error code standards
- Transport compatibility
- Schema enforcement
- Version management
- Backward compatibility
- Standards documentation

Development tooling:
- IDE configurations
- Debugging tools
- Testing frameworks
- Code generators
- Documentation tools
- Deployment scripts
- Monitoring dashboards
- Performance profilers

Community engagement:
- Open source contributions
- Documentation improvements
- Example implementations
- Best practice sharing
- Issue resolution
- Feature discussions
- Standards participation
- Knowledge transfer
