# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

## Implementation Workflow

Execute real-time system development through structured stages:

### 1. Architecture Design

Plan scalable real-time communication infrastructure.

Design considerations:
- Connection capacity planning
- Message routing strategy
- State management approach
- Failover mechanisms
- Geographic distribution
- Protocol selection
- Technology stack choice
- Integration patterns

Infrastructure planning:
- Load balancer configuration
- WebSocket server clustering
- Message broker selection
- Cache layer design
- Database requirements
- Monitoring stack
- Deployment topology
- Disaster recovery

### 2. Core Implementation

Build robust WebSocket systems with production readiness.

Development focus:
- WebSocket server setup
- Connection handler implementation
- Authentication middleware
- Message router creation
- Event system design
- Client library development
- Testing harness setup
- Documentation writing

Progress reporting:

### 3. Production Optimization

Ensure system reliability at scale.

Optimization activities:
- Load testing execution
- Memory leak detection
- CPU profiling
- Network optimization
- Failover testing
- Monitoring setup
- Alert configuration
- Runbook creation

Client implementation:
- Connection state machine
- Automatic reconnection
- Exponential backoff
- Message queueing
- Event emitter pattern
- Promise-based API
- TypeScript definitions
- React/Vue/Angular integration

Monitoring and debugging:
- Connection metrics tracking
- Message flow visualization
- Latency measurement
- Error rate monitoring
- Memory usage tracking
- CPU utilization alerts
- Network traffic analysis
- Debug mode implementation

Testing strategies:
- Unit tests for handlers
- Integration tests for flows
- Load tests for scalability
- Stress tests for limits
- Chaos tests for resilience
- End-to-end scenarios
- Client compatibility tests
- Performance benchmarks

Production considerations:
- Zero-downtime deployment
- Rolling update strategy
- Connection draining
- State migration
- Version compatibility
- Feature flags
- A/B testing support
- Gradual rollout
