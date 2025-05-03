# openDispatch Hackathon Plan

**Team:**
- Juan Palomino (Software Engineer)
- Ximena Bustamante (Data Analyst)

**Goal:**
Deliver a working demo by 4:15pm showing calls coming into a dispatch center, being routed by a dispatcher agent to one of three sub-agents (Public Works, Animal Control, Waste Management), and tracking conversations from call-in to dispatching services.

---

## Schedule: 1:30pm – 4:15pm

### 1:30 – 1:45pm (15 min)
- **Team Sync & Architecture**
  - Review requirements, clarify demo flow
  - Sketch system architecture (call flow, agents, Azure setup)
  - Assign initial tasks

### 1:45 – 2:30pm (45 min)
- **Juan:**
  - Set up Azure environment and voice agent infrastructure
  - Scaffold dispatcher agent and sub-agent services (Public Works, Animal Control, Waste Management)
  - Implement basic call routing logic
- **Ximena:**
  - Define data schema for call tracking (caller ID, timestamps, agent routing, conversation logs)
  - Prepare mock data for demo/testing
  - Research and outline analytics/metrics for demo

### 2:30 – 3:15pm (45 min)
- **Juan:**
  - Integrate call tracking and metadata logging
  - Implement conversation logging between dispatcher and sub-agents
  - Build simple UI or CLI for demo (if time allows)
- **Ximena:**
  - Set up data storage (spreadsheet, database, or Azure Table)
  - Implement data collection for calls and agent interactions
  - Start preparing demo visualizations (call flow, agent activity)

### 3:15 – 3:45pm (30 min)
- **Juan:**
  - Polish call routing logic (configurable sub-agents)
  - Test end-to-end call flow
  - Fix bugs, improve stability
- **Ximena:**
  - Finalize analytics/metrics dashboard or summary
  - Prepare talking points for demo (impact, insights)

### 3:45 – 4:00pm (15 min)
- **Integration & Dry Run**
  - Connect data tracking/analytics to live demo
  - Run through demo script together
  - Identify and fix last-minute issues

### 4:00 – 4:15pm (15 min)
- **Final Demo Prep & Delivery**
  - Ensure system is live and stable
  - Deliver demo to judges, answer questions

---

## Demo Requirements Checklist
- [ ] Dispatcher agent accepts incoming calls
- [ ] Calls routed to one of three configurable sub-agents:
    - Public Works (catch-all)
    - Animal Control
    - Waste Management
- [ ] All calls and conversations are tracked (with metadata)
- [ ] Demo shows end-to-end flow from call-in to dispatch
- [ ] Analytics/metrics or conversation logs are available for demo

---

**Let’s build openDispatch!**
