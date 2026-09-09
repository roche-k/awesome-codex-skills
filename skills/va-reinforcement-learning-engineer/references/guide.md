# Domain guide

Apply the relevant sections to the actual request. This adapted source is
a menu of domain considerations, not a requirement to perform every item.
Source version numbers and numeric targets are historical examples; use the
project's real versions and agreed acceptance criteria. Check current primary
documentation before relying on external APIs, standards, or provider behavior.
Tool labels describe operations and do not grant unavailable tools or services.

RL engineer checklist:
- Environment validated and reproducible
- Reward function designed properly
- Algorithm selected appropriately
- Training stability verified consistently
- Hyperparameters tuned thoroughly
- Evaluation metrics tracked completely
- Policy deployed successfully
- Safety constraints enforced effectively

Environment design:
- State space definition
- Action space modeling
- Reward shaping
- Episode termination
- Observation normalization
- Multi-agent setup
- Procedural generation
- Domain randomization

Algorithm expertise:
- Deep Q-Networks (DQN)
- Proximal Policy Optimization (PPO)
- Soft Actor-Critic (SAC)
- Twin Delayed DDPG (TD3)
- Advantage Actor-Critic (A2C/A3C)
- REINFORCE variants
- Model-based methods (Dreamer/MuZero)
- Offline RL (CQL/IQL)

Reward engineering:
- Reward shaping strategies
- Intrinsic motivation
- Curiosity-driven exploration
- Sparse reward handling
- Multi-objective rewards
- Reward normalization
- Hindsight experience replay
- Inverse RL techniques

Policy optimization:
- Policy gradient methods
- Value function approximation
- Actor-critic architectures
- Trust region methods
- Entropy regularization
- Gradient clipping
- Learning rate schedules
- Batch size strategies

Training infrastructure:
- Vectorized environments
- Parallel rollout collection
- Distributed training
- GPU acceleration
- Experience replay buffers
- Prioritized sampling
- Checkpoint management
- Experiment tracking

Exploration strategies:
- Epsilon-greedy methods
- Boltzmann exploration
- Noise injection (OU/Gaussian)
- Count-based exploration
- Random network distillation
- Go-Explore techniques
- Upper confidence bounds
- Thompson sampling

Multi-agent RL:
- Cooperative strategies
- Competitive training
- Self-play methods
- Communication protocols
- Centralized training
- Decentralized execution
- Emergent behaviors
- Population-based training

Sim-to-real transfer:
- Domain randomization
- System identification
- Progressive networks
- Transfer learning
- Reality gap analysis
- Calibration methods
- Safety validation
- Deployment monitoring

Framework ecosystem:
- Stable-Baselines3
- RLlib / Ray
- Gymnasium / Farama
- CleanRL
- TorchRL
- JAX-based (PureJaxRL)
- Unity ML-Agents
- Isaac Gym / Sim

## Development Workflow

Execute RL development through systematic phases:

### 1. Problem Formulation

Design the RL problem and environment.

Formulation priorities:
- MDP definition
- State representation
- Action space design
- Reward function
- Episode structure
- Safety constraints
- Evaluation protocol
- Success criteria

Environment design:
- Define observations
- Model dynamics
- Shape rewards
- Set terminations
- Validate physics
- Benchmark baselines
- Test edge cases
- Document interfaces

### 2. Implementation Phase

Build and train RL agents.

Implementation approach:
- Create environment
- Implement agent architecture
- Configure training loop
- Tune hyperparameters
- Monitor convergence
- Evaluate performance
- Optimize efficiency
- Deploy policy

RL patterns:
- Curriculum learning
- Reward curriculum
- Self-play training
- Imitation pretraining
- Offline-to-online
- Hierarchical policies
- Goal-conditioned agents
- Ensemble methods

### 3. RL Excellence

Deliver robust, deployable RL systems.

Excellence checklist:
- Environment validated
- Training converged
- Policy robust
- Evaluation thorough
- Safety verified
- Generalization tested
- Documentation complete
- Deployment automated

Training excellence:
- Convergence stable
- Sample efficiency high
- Reward maximized
- Variance controlled
- Exploration balanced
- Overfitting prevented
- Resources optimized
- Reproducibility ensured

Evaluation excellence:
- Multiple seeds tested
- Statistical significance
- Out-of-distribution tested
- Adversarial evaluation
- Human baselines compared
- Ablation studies done
- Failure modes analyzed
- Reports generated

Safety excellence:
- Constraints enforced
- Reward hacking prevented
- Safe exploration
- Bounded actions
- Fallback policies
- Monitoring active
- Anomaly detection
- Human oversight

Deployment excellence:
- Policy exported
- Inference optimized
- Latency acceptable
- Monitoring active
- Rollback ready
- A/B testing enabled
- Scaling configured
- Alerts established

Best practices:
- Reproducible experiments
- Seed management
- Hyperparameter logging
- Tensorboard monitoring
- Weights & Biases tracking
- Version control
- Modular codebase
- Thorough documentation
