## Arkham Intelligence API

Enrich an Ethereum address with Arkham's blockchain intelligence.

**Input:**
```
0x3a9F7ab2B042242097c5d51922Aa82e70c7991ca
```

**Endpoint:**
```
https://api.arkhamintelligence.com/intelligence/address/{address}/all
```

Arkham has publicly documented this endpoint as taking an address and returning intelligence associated with it.

**Authentication:**
```
API-key: <ARKHAM_API_KEY>
```

**Expected information:**
* Entity name / entity attribution
* Address labels/tags
* chain/address intelligence
* Related counterparties and attribution data

Arkham's current API is built around addresses, entities, labels, and tags, with attribution treated as confidence-based intelligence rather than an absolute claim.

**Cost/access:**
```
Paid / API access required
Per-endpoint credits/billing
```

Arkham currently advertises flexible API usage and API access through its API program; its documentation explicitly covers credit pricing and billing.

**Implementation status:**
```
❌ Not executed
```

**Reason:**
```
API access requires an appropriate Arkham API
subscription/access. No paid API access was available
for this task.
```

**Planned pipeline:**
```
Address CSV
     ↓
Validate address
     ↓
Arkham API
     ↓
/intelligence/address/{address}/all
     ↓
Entity + Labels/Tags + Counterparties
     ↓
Structured output CSV/JSON
```