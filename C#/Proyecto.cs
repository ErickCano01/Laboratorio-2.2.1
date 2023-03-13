using System;

public class Proyecto {
	private String nombre;
	private String fechaInicio;
	private Boolean estado;

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

	private Tareas[] tareas;

	private Equipo[] equipos;
	private Stakeholder[] stakeholders;

}
