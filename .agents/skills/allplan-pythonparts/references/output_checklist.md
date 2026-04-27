# Output Checklist

- [ ] Contract chosen correctly (Standard / Script Object / Interactor)
- [ ] Required entry points exist for selected contract
- [ ] `.py` and `.pyp` exist as a matching pair
- [ ] Parameter names are exactly consistent between `.pyp` and `build_ele.<Name>.value`
- [ ] Units are millimeters and labels are explicit
- [ ] No known hallucinated API calls are used
- [ ] Boolean ops unpack tuple return (`err, result = ...`)
- [ ] Error handling and logs are explicit (no silent pass)
- [ ] Validation script returns pass
- [ ] Manual smoke tests in Allplan are documented
