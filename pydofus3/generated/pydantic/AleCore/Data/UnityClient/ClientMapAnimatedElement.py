from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientMapElement import ClientMapElement

class ClientMapAnimatedElement(ClientMapElement):
	cellId: int
	playAnimation: bool
	playAnimStatic: bool
	playerGuildCustomisable: bool
	requiresServerUpdate: bool
	minDelay: int
	maxDelay: int
	isStagingTarget: bool
	stagingId: str
	background: bool
	displayOrder: int

