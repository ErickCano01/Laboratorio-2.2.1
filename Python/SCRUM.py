from Proyecto import Proyecto
from Stakeholder import Stakeholder
from ScrumMaster import ScrumMaster
from Equipo import Equipo
from Integrante import Integrante

proyecto = Proyecto("Proyecto 1", "20-19-2023", True)

guillermo = Stakeholder(100, "memo", 0)
proyecto.stakeholders.append(guillermo)

pepe = ScrumMaster("pepe")
equipo = Equipo("Bum Bum", 0, pepe)

juan = Integrante("Juan", "Diseñador")
equipo.integrantes.append(juan)

leo = Integrante("Leo", "Analista")
equipo.integrantes.append(leo)

proyecto.equipos.append(equipo)

print(proyecto)