Stakeholder stakeholder = new Stakeholder(0,"Pablo",500f);
Integrante integrante = new Integrante("Pepe","Programador");
ScrumMaster scrumMaster = new ScrumMaster("lalo", "Diseñador");
Equipo equipo = new Equipo(1,"Equipo dinamita",scrumMaster, integrante);
Tareas tareas = new Tareas(1,5,"Realizar x cosa", integrante);
Proyecto proyecto = new Proyecto("Hola", "12/03/2023", true, tareas, equipo, stakeholder);

Console.WriteLine(proyecto);
