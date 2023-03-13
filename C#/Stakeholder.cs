using System;

public class Stakeholder {
	private float presupuesto;
	private String nombre;
	private int id;

	public float GetPresupuesto() {
		return this.presupuesto;
	}
	public void SetPresupuesto(ref float presupuesto) {
		this.presupuesto = presupuesto;
	}
	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public int GetId() {
		return this.id;
	}
	public void SetId(ref int id) {
		this.id = id;
	}


}
