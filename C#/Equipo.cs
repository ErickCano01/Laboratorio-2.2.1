using System;

public class Equipo {
	private String nombre;
	private int id;
	private ScrumMaster scrumMaster;

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
	public void AddIntegrate(ref Integrante integrante) {
		throw new System.NotImplementedException("Not implemented");
	}
	public void ToString() {
		throw new System.NotImplementedException("Not implemented");
	}
	public ScrumMaster GetScrumMaster() {
		return this.scrumMaster;
	}
	public void SetScrumMaster(ref ScrumMaster scrumMaster) {
		this.scrumMaster = scrumMaster;
	}
	public Equipo(ref int id, ref String nombre, ref ScrumMaster sm) {
		throw new System.NotImplementedException("Not implemented");
	}

	private Integrante[] integrantes;

}
