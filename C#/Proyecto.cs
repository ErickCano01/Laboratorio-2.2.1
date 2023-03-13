using System;

public class Proyecto {
	private String nombre;
	private String fechaInicio;
	private Boolean estado;
    private Tareas tareas;
	private Equipo equipos;
	private Stakeholder stakeholder;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public String GetFechaInicio() {
		return this.fechaInicio;
	}
	public void SetFechaInicio(ref String fechaInicio) {
		this.fechaInicio = fechaInicio;
	}
	public Boolean GetEstado() {
		return this.estado;
	}
	public void SetEstado(ref Boolean estado) {
		this.estado = estado;
	}
    public Proyecto(String nombre, String fechaInicio, Boolean estado, Tareas tareas, Equipo equipos, Stakeholder stakeholder){
        this.nombre = nombre;
        this.fechaInicio = fechaInicio;
        this.estado = estado;
        this.tareas = tareas;
        this.equipos = equipos;
        this.stakeholder = stakeholder;
    }
    public override String ToString() {
		return base.ToString() + "\n" + "Nombre del proyecto: "+ nombre.ToString() + "\n" + "Fecha de inicio: " + fechaInicio.ToString() +"\n"
        + "Estado: " + estado.ToString() +"\n" +"Tareas: "+ "\n" + tareas.ToString() +"\n"
        + "equipos : "+ "\n" + equipos.ToString() +"\n" + "StakeHolder : "+ "\n" + stakeholder.ToString() +"\n";
	}

}