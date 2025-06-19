# Technical Reality Constraints
*Created after systematic AI capability overestimation in 65% of failed proposals*

## Purpose
Prevent technical unfeasibility that contributed to 0% survival rate in adversarial evaluation.

## The Core Problem

**What Failed**: Overestimating current AI capabilities and underestimating technical complexity
**What Works**: Building within proven web stack capabilities with standard APIs

## Current AI Capability Reality Check

### What AI CAN Do Reliably (2025)
✅ **Text Generation**: High-quality content, documentation, code
✅ **Data Processing**: Parsing, transformation, basic analysis
✅ **API Integration**: Connecting to established services
✅ **Web Development**: Full-stack applications with standard frameworks
✅ **Basic Automation**: Workflows, email sequences, data entry
✅ **Simple Personalization**: Rule-based customization, content matching

### What AI CANNOT Do Reliably (2025)
❌ **Real-time Voice Recognition**: Especially with accents, background noise
❌ **Complex Video Processing**: Beyond basic transcription/metadata
❌ **Predictive Analytics**: "AI predicts future trends" claims
❌ **Medical Diagnosis**: Any health assessment or advice
❌ **Financial Calculations**: Requiring certification or regulatory compliance
❌ **Legal Interpretation**: Compliance, contract analysis, regulatory guidance
❌ **Real-time Data Analysis**: Requiring expensive streaming APIs
❌ **Native Mobile Apps**: iOS/Android development beyond web views

## Approved Technical Stack

### Core Framework (Proven with Claude CODE)
- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Backend**: Supabase (database, auth, APIs)
- **Hosting**: Vercel (frontend), Supabase (backend)
- **Payment**: Stripe (standard integration)
- **Email**: Resend, SendGrid (transactional)
- **Analytics**: PostHog, Simple Analytics (privacy-focused)

### Approved Integrations
**Low-Cost APIs** (<$50/month at scale):
- Stripe (payments)
- Gmail API (email automation)
- Calendar APIs (Google, Outlook)
- Slack/Discord (notifications)
- GitHub (code management)
- Zapier (workflow automation)

**Medium-Cost APIs** ($50-200/month at scale):
- OpenAI (text generation - sparingly)
- Anthropic Claude (when needed)
- Simple transcription services
- Basic image processing (Cloudinary)

### Forbidden Technologies
❌ **Native Mobile Development**: React Native, Swift, Kotlin
❌ **Real-time Video/Audio**: WebRTC, streaming protocols
❌ **Machine Learning Training**: Custom ML models, training pipelines
❌ **IoT Integration**: Hardware devices, sensors, embedded systems
❌ **AR/VR**: Three.js beyond basic use, Unity, VR frameworks
❌ **Blockchain/Crypto**: Smart contracts, wallet integrations
❌ **Desktop Applications**: Electron apps, native desktop

## Development Complexity Guidelines

### Simple (2-4 weeks) ✅
- CRUD applications with database
- User authentication and profiles
- Subscription management
- Basic dashboard with charts
- Email automation workflows
- Simple API integrations
- Content management systems

### Medium (4-8 weeks) ⚠️
- Multi-tenant applications
- Complex user roles/permissions
- Real-time features (basic chat, notifications)
- Payment processing with multiple plans
- Integration with 3-5 external APIs
- Advanced search and filtering
- Basic reporting and analytics

### Complex (8+ weeks) ❌
- Real-time collaboration tools
- Complex data processing pipelines
- Multi-step workflow engines
- Advanced AI/ML integration
- High-frequency trading systems
- Video/audio processing
- Multi-platform synchronization

## API Cost Reality Check

### Budget-Friendly APIs
- Basic email: $0-20/month
- Standard databases: $0-50/month
- Simple integrations: $10-30/month each
- Analytics: $0-25/month

### Expensive APIs (Avoid)
- Real-time financial data: $500+/month
- Advanced AI models: $200+/month at scale
- Video processing: $300+/month
- Voice recognition: $100+/month
- Maps with high usage: $200+/month

## Technical Feasibility Validation Process

**For every proposed solution**:

1. **Feature Mapping**:
   - List all core features
   - Map each to approved technology
   - Identify any forbidden technologies
   - Flag medium/complex development items

2. **API Requirements**:
   - List all external integrations needed
   - Research actual API costs
   - Confirm APIs exist and are accessible
   - Calculate monthly cost at 100+ customers

3. **Development Estimate**:
   - Count database models needed
   - List user interfaces required
   - Estimate integration complexity
   - Confirm timeline under 8 weeks

4. **Maintenance Reality**:
   - What breaks when APIs change?
   - Customer support automation level
   - Scaling considerations
   - Update/maintenance requirements

## Red Flag Technical Claims

**Auto-Reject These Phrases**:
- "AI-powered prediction engine"
- "Real-time voice analysis"
- "Advanced machine learning algorithms"
- "Predictive analytics dashboard"
- "Voice-first interface"
- "Computer vision capabilities"
- "Native mobile experience"
- "Real-time video processing"
- "Advanced AI recommendations"

**Approved Technical Claims**:
- "Web-based dashboard"
- "Automated workflows"
- "API integrations"
- "Content generation"
- "Data aggregation"
- "User management"
- "Subscription billing"
- "Email automation"

## Technical Feasibility Checklist

**Pass Criteria** (all must be met):
- [ ] Buildable with approved tech stack
- [ ] No forbidden technologies required
- [ ] API costs under $200/month at scale
- [ ] Development timeline under 8 weeks
- [ ] All integrations confirmed available
- [ ] No "advanced AI" claims beyond text generation
- [ ] Maintenance complexity manageable

**Auto-Reject Triggers**:
- Requires native mobile apps
- Needs real-time video/audio processing
- Claims predictive capabilities
- Requires expensive APIs (>$200/month)
- Development estimate over 8 weeks
- Depends on training custom ML models

## Implementation

**In Ideation Process**:
1. Map solution to approved technologies first
2. Research API availability and costs
3. Estimate development complexity
4. Document technical feasibility evidence
5. Include "Technical Feasibility" section in proposals

**Quality Gate**:
Every proposal must include technical validation confirming solution is buildable within constraints before adversarial evaluation.

---

*This framework prevents technical overoptimism that contributed to 65% of proposal failures by enforcing realistic capability constraints.*