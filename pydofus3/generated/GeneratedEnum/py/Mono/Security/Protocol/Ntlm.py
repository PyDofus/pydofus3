from enum import IntFlag

# Mono.Security.Protocol.Ntlm.NtlmAuthLevel
class NtlmAuthLevel(IntFlag):
    LM_and_NTLM = 0
    LM_and_NTLM_and_try_NTLMv2_Session = 1
    NTLM_only = 2
    NTLMv2_only = 3

# Mono.Security.Protocol.Ntlm.NtlmFlags
class NtlmFlags(IntFlag):
    NegotiateUnicode = 1
    NegotiateOem = 2
    RequestTarget = 4
    NegotiateNtlm = 512
    NegotiateDomainSupplied = 4096
    NegotiateWorkstationSupplied = 8192
    NegotiateAlwaysSign = 32768
    NegotiateNtlm2Key = 524288
    Negotiate128 = 536870912
    Negotiate56 = -2147483648

