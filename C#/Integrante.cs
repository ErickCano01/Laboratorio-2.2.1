using System;

public class Integrante {
	private String nombre;
	private String rol;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public String GetRol() {
		return this.rol;
	}
	public void SetRol(ref String rol) {
		this.rol = rol;
	}
	public void ToString() {
		throw new System.NotImplementedException("Not implemented");
	}
	public Integrante(ref String nombre, ref String rol) {
		throw new System.NotImplementedException("Not implemented");
	}

	private Equipo equipo;
	private Tareas[] tareas;

}
